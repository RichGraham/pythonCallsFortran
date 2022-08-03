for f in Tests*.ipynb;
do
    ipythToPython.sh  $f
done

coverage erase
for f in Tests*.py
do
   echo $f
   coverage run -a $f
done

coverage report
