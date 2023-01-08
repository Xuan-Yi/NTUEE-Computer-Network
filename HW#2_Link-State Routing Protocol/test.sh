#! C:\Windows\System32\bash.exe

g++ lib/compare.cpp -O2 -o compare

# remove outputs
for output_file in testcase/*_GenTable.txt; do
    rm $output_file
done
rm testcase/p1_test1_RmRouter2.txt
rm testcase/p1_test2_RmRouter3.txt 
wait

# part1
echo "part1"
for filename in testcase/*.txt; do
    python hw2.py "$filename" 
done
wait

# part1 comparison
for output_file in testcase/*_GenTable.txt; do
    golden_file="testcase/goldens/$(basename "$output_file" _GenTable.txt)_golden.txt"
    # python lib/test.py $output_file $golden_file
    # ./compare $output_file $golden_file
    if cmp -s "$output_file" "$golden_file"; then
        printf 'The file "%s" is the same as "%s"\n' "$output_file" "$golden_file"
    else
        printf 'The file "%s" is different from "%s"\n' "$output_file" "$golden_file"
        diff $output_file $golden_file
    fi
done
wait

# part2
echo "part2"
python hw2.py testcase/p1_test1.txt 2
python hw2.py testcase/p1_test2.txt 3
wait

# part2 comparison
output_file=testcase/p1_test1_RmRouter2.txt
golden_file=testcase/goldens/p2_test1_golden_rm2.txt
if cmp -s "$output_file" "$golden_file"; then
    printf 'The file "%s" is the same as "%s"\n' "$output_file" "$golden_file"
else
    printf 'The file "%s" is different from "%s"\n' "$output_file" "$golden_file"
    diff $output_file $golden_file
fi
output_file=testcase/p1_test2_RmRouter3.txt
golden_file=testcase/goldens/p2_test2_golden_rm3.txt
if cmp -s "$output_file" "$golden_file"; then
    printf 'The file "%s" is the same as "%s"\n' "$output_file" "$golden_file"
else
    printf 'The file "%s" is different from "%s"\n' "$output_file" "$golden_file"
    diff $output_file $golden_file
fi
# python lib/test.py testcase/p1_test1_RmRouter2.txt testcase/goldens/p2_test1_golden_rm2.txt
# python lib/test.py testcase/p1_test2_RmRouter3.txt testcase/goldens/p2_test2_golden_rm3.txt
# ./compare testcase/p1_test1_RmRouter2.txt testcase/goldens/p2_test1_golden_rm2.txt
# ./compare testcase/p1_test2_RmRouter3.txt testcase/goldens/p2_test2_golden_rm3.txt

rm compare

exit