for f in Tests*.py
do
   echo $f
   python $f
   echo ''
done
