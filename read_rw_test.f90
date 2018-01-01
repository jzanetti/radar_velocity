program read_rw_test
 implicit none
 integer, parameter :: mxmn=35, mxlv=1000
 integer        :: unit_in=10
 integer        :: numrwbin, ntb
 integer        :: i, istat
 real(8) :: hdr(mxmn),hdr2(mxmn),hdr3(mxmn),obs(3,mxlv)
 real(8)        :: rstation_id
 integer        :: valid_time

 open(unit_in,file='l2rwbufr.bin',form='unformatted',status='old')
 read(unit_in,iostat=istat) ntb
 read(unit_in,iostat=istat) numrwbin
 read(unit_in,iostat=istat) (hdr(i),i=1,8)

 read(unit_in) (hdr2(i),i=1,6)
 read(unit_in) (hdr3(i),i=1,4)
 do i=1,numrwbin
   read(unit_in) obs(1:3,i)
 enddo

 rstation_id=hdr(1)
 valid_time=(int(hdr2(1))*1000000)+ &
               (int(hdr2(2))*10000)+ &
               (int(hdr2(3))*100)+(int(hdr2(4)))

 write(*,*) 'rstation_id: ', rstation_id
 write(*,*) 'valid_time: ', valid_time
 close(unit_in)

end program
