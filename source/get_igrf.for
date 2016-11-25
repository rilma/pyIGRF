
      subroutine get_igrf(xlat,xlon,height,year,dirdata,bnorth,beast
     . ,bdown,xl,icode)

!-------------------------------------------------------------------------------
!  Input:  Entry point 
!               xlat  -> Geodetic latitude in degrees (north)
!               xlon  -> Geodetic longitude in degrees (east)
!               height -> Altitude above sea level in km
!               year  -> decimal year (year + month/12. - 0.5 or 
!                        year + day-of-year/365 or 366 if leap year) 
!-------------------------------------------------------------------------------
!  Output: 'bnorth', 'beast', and 'bdown' are the strength of the magnetic 
!          field components (in Gauss) with respect to the local geodetic 
!          coordinate systems, with axis pointing in the tangential plane to 
!          the north, east and downward direction.
!        	xl    -> L value
!	        icode -> =1  L is correct; =2  L is not correct;
!		         =3  an approximation is used
!

      real xlat,xlon,height,year
      real bnorth,beast,bdown,xl
      integer icode

      character*256 dirdata, dirdata1

      real dimo,babs,bab1

Cf2py intent(in) xlat,xlon,height,year,dirdata
Cf2py intent(out) bnorth,beast,bdown,xl,icode
      
      common /GENER/ UMR,ERA,AQUAD,BQUAD

      common /folders/ dirdata1
      dirdata1 = trim(dirdata)

      call initize
      call feldcof(year,dimo)     
      call feldg(xlat,xlon,height,bnorth,beast,bdown,babs)
      call shellg(xlat,xlon,height,dimo,xl,icode,bab1)

      end
