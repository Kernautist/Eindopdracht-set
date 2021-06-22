for f in ./*.png
do
	name="${f%.*}"
	echo $name
	convert $name."png"  -rotate 90 $name."gif"
done