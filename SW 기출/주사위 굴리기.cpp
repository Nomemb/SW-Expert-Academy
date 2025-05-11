/*
https://www.acmicpc.net/problem/14499
N * M 인 지도 존재. 오른쪽: 동, 위쪽: 북
주사위 굴렸을 때 이동한 칸의 수가 0이면 칸에 주사위 바닥면이 복사됨.
0이 아닌 경우 칸에 쓰여있는 수가 주사위 바닥에 복사됨. 칸은 0으로 변함.
주사위 좌표와 이동 명령이 주어졌을 때 이동할 때마다 상단에 쓰인 값을 구하라.
주사위는 지도의 밖으로 이동할 수 없음.

이동명령: 동1 서2 북3 남4
N: 세로, M: 가로, x,y 주사위 좌표, K: 명령 개수
*/

#include <bits/stdc++.h>
#define MAX 20
using namespace std;

int N, M, x, y, K;
int arr[MAX][MAX];
vector<int> dice(6, 0);

bool isValid(const int order)
{
    if (order == 1)
        return y + 1 < M;
    if (order == 2)
        return y - 1 >= 0;
    if (order == 3)
        return x - 1 >= 0;
    if (order == 4)
        return x + 1 < N;
    return false;
}

vector<int> rollDice(vector<int>& vec, const int order)
{
    int tmp = vec[2];
    // 동쪽 회전
    if (order == 1)
    {
        y++;
        vec[2] = vec[1];
        vec[1] = vec[3];
        vec[3] = tmp;
    }
    // 서쪽 회전
    else if (order == 2)
    {
        y--;
        vec[2] = vec[3];
        vec[3] = vec[1];
        vec[1] = tmp;
    }
    // 북쪽 회전
    else if (order == 3)
    {
        x--;
        vec[2] = vec[4];
        vec[4] = vec[5];
        vec[5] = vec[0];
        vec[0] = tmp;
    }
    // 남쪽 회전
    else if (order == 4)
    {
        x++;
        vec[2] = vec[0];
        vec[0] = vec[5];
        vec[5] = vec[4];
        vec[4] = tmp;
    }
    else
    {
        cout << "Invalid Order" << endl;
    }

    return vec;
}

vector<int> split(const string& line)
{
    istringstream iss(line);
    vector<int> result;
    int number;

    while (iss >> number)
        result.push_back(number);

    return result;
}

int main()
{
    // 변수 입력
    cin >> N >> M >> x >> y >> K;
    cin.ignore();
    string inputString;

    // 지도 각 칸 값 입력
    for (auto i = 0; i < N; i++)
    {
        getline(cin, inputString);
        vector<int> nums = split(inputString);
        for (size_t j = 0; j < nums.size(); j++)
            arr[i][j] = nums[j];
    }

    string orderInput;
    getline(cin, orderInput);
    vector<int> orders = split(orderInput);

    for (int order : orders)
    {
        if (!isValid(order))
            continue;

        dice = rollDice(dice, order);
        if (arr[x][y] == 0)
        {
            arr[x][y] = dice[5];
        }
        else
        {
            dice[5] = 0;
            arr[x][y] = dice[5];
        }
        cout << dice[2] << endl;
    }
}
