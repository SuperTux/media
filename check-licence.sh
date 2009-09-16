d=$1

if [ -z $d ]
then
    d=.
fi

for file in `find $d -iregex '.*\.\(ogg\|wav\)'`
do
    licence=`svn propget licence "$file"`

    echo "$file" - "$licence"
done
