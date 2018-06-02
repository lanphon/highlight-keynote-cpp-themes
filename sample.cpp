#include<iostream>

#ifdef TEST_SAMPLE
#define TEST_SAMPLES_DEFINITION
#endif

#include<stdint.h>
#include<string>

struct sample0
{
	typedef my_integer int64_t;

	uint32_t i;
	uint32_t j;
};

int main(int argc, char **argv)
{
	using namespace std;

	string str_sample = "just a sample string";

	cout << str_sample << endl;
}
