#include <cstdio>
#include <vector>
#include <cstdint>
#include <cstdlib>
#include <cmath>
#include <limits>

extern "C" {
#include <fftw3.h>
}

void freq_est (std::vector< std::pair< double, double > >& vals, double freq) {

    uint32_t i = 0, nc = 0, max_i = 0;
    double max_mag = 0.0, tgt_freq = 0.0;
    fftw_complex *out;
    fftw_plan plan_forward;
    std::vector< double > ivals;

    for (int i = 0; i < vals.size (); ++i) {
        ivals.push_back (vals[i].first);
    }

    nc = ivals.size ();

    out = (fftw_complex *)fftw_malloc ( sizeof ( fftw_complex ) * nc );
    if (NULL == out) {
        fprintf (stderr, "Failed to allocate memory to compute FFT\n");
        exit (-2);
    }

    plan_forward = fftw_plan_dft_r2c_1d ( nc, &ivals[0], out, FFTW_ESTIMATE );
    fftw_execute ( plan_forward );

    double thresh = 0.0;

    /* Ignore DC frequency @ i == 0 */
    for ( i = 1; i < nc; i++ )
    {
        /* Magnitude = sqrt(R*R + I*I) */
        double magnitude = sqrt(out[i][0] * out[i][0] + out[i][1] * out[i][1]);
        if (magnitude > max_mag) {
            max_i = i;
            max_mag = magnitude;
            thresh = 20 * log10 (max_mag * max_mag);
        }
    }

    tgt_freq = max_i * freq / ivals.size ();

    double signal = 0.0;
    double noise = 0.0;
    double noise_all = 0.0;

#ifdef USE_THRESH
    for ( i = 0; i < nc; i++ )
    {
        double magnitude = sqrt(out[i][0] * out[i][0] + out[i][1] * out[i][1]);
        if (magnitude > thresh) {
            signal += magnitude * magnitude;
        } else {
            if (i < nc / 2) {
                noise += magnitude * magnitude;
            }
            noise_all += magnitude * magnitude;
        }
    }
#endif
#ifdef USE_MAX
    for ( i = 0; i < nc; i++ )
    {
        double magnitude = sqrt(out[i][0] * out[i][0] + out[i][1] * out[i][1]);
        if (i == max_i) {
            signal += magnitude * magnitude;
        } else {
            if (i < nc / 2) {
                noise += magnitude * magnitude;
            }
            noise_all += magnitude * magnitude;
        }
    }
#endif
#define USE_HARMONICS
#ifdef USE_HARMONICS
    for ( i = 0; i < nc; i++ )
    {
        double magnitude = sqrt(out[i][0] * out[i][0] + out[i][1] * out[i][1]);
        double i_freq = i * freq / ivals.size ();
        uint32_t rem = static_cast< uint32_t >(i_freq) % static_cast< uint32_t >(tgt_freq);
        /* Add any harmonic as signal */
        if (i > 0 && 0 == rem) {
            //printf ("Harmonic: %0.4f\n", i_freq);
            signal += magnitude * magnitude;
        } else {
            if (i < nc / 2) {
                noise += magnitude * magnitude;
            }
            noise_all += magnitude * magnitude;
        }
    }
#endif

    fftw_destroy_plan ( plan_forward );
    fftw_free ( out );


    double snr = 10 * log10 (signal / noise);
    double snr_all = 10 * log10 (signal / noise_all);

    printf ("freq:%0.4f snr:%0.4f snra:%0.4f\n", tgt_freq, snr, snr_all);
}

template< typename T >
std::vector< std::pair< double, double > > read_data (const char *fname, const char *out) {
    FILE *fin = fopen(fname, "rb");
    FILE *fout = fopen(out, "wb");
    std::vector< std::pair< double, double > > data;
    T ival = 0, qval = 0;
    double max_val = std::numeric_limits< T >::max ();
    fprintf (fout, "I,Q\n");
    while (! feof (fin) && ! ferror (fin)) {
        fread (&ival, sizeof (T), 1, fin);
        if (feof (fin)) { break; }
        fread (&qval, sizeof (T), 1, fin);
        data.push_back (std::make_pair< double, double> (ival / max_val, qval / max_val));
        fprintf (fout, "%0.4f,%0.4f\n", 
                static_cast< double >(ival) / max_val, static_cast< double >(qval) / max_val);
        if (feof (fin)) { break; }
    }
    fclose (fout);
    fclose (fin);
    return data;
}


int main () {
    double sample_freq = 100000.0;
    //std::vector< std::pair< double, double > > data8 = 
    //    read_data< int8_t > ("index.html", "i8.csv");
    //freq_est (data8, sample_freq);
    //std::vector< std::pair< double, double > > data16 = 
    //    read_data< int16_t > ("index.html", "i16.csv");
    //freq_est (data16, sample_freq);
    std::vector< std::pair< double, double > > data32 = 
        read_data< int32_t > ("index.html", "i32.csv");
    freq_est (data32, sample_freq);
    return 0;
}
