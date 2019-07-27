/* -*- c++ -*- */
/*
 * Copyright 2008,2012 Free Software Foundation, Inc.
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_ANALOG_CPFSK_BC_H
#define INCLUDED_ANALOG_CPFSK_BC_H

#include <gnuradio/analog/api.h>
#include <gnuradio/sync_interpolator.h>

namespace gr {
  namespace analog {

    /*!
     * \brief Perform continuous phase 2-level frequency shift keying modulation
     * on an input stream of unpacked bits.
     * \ingroup modulators_blk
     * \ingroup deprecated_blk
     */
    class ANALOG_API cpfsk_bc : virtual public sync_interpolator
    {
    public:
      // gr::analog::cpfsk_bc::sptr
      typedef boost::shared_ptr<cpfsk_bc> sptr;

      /*!
       * \brief Make a CPFSK block.
       *
       * \param k modulation index
       * \param ampl output amplitude
       * \param samples_per_sym	number of output samples per input bit
       */
      static sptr make(float k, float ampl, int samples_per_sym);

      virtual void set_amplitude(float amplitude) = 0;
      virtual float amplitude() = 0;
      virtual float freq() = 0;
      virtual float phase() = 0;
    };

  } /* namespace analog */
} /* namespace gr */

#endif /* INCLUDED_ANALOG_CPFSK_BC_H */

/* ! BlockTool
input_signature: make
input_min_streams: 1
input_max_streams: 1
input_sizeof_stream_item: sizeof(char)
output_signature: make
output_min_streams: 1
output_max_streams: 1
output_sizeof_stream_item: sizeof(gr_complex)
message_input: 
message_output: 
EndTool !*/
