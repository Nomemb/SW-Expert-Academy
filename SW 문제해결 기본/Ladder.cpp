#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <queue>
using namespace std;

#define MAX 100

int tmp;
int LADDER[MAX][MAX];
bool visited[MAX][MAX];
int dx[] = { 0, 0, -1};
int dy[] = { -1, 1, 0};

void input()
{
    cin >> tmp;
    cin.ignore();

    memset(LADDER, 0, sizeof(LADDER));
    memset(visited, false, sizeof(visited));

    string line;

    int num;
    for (int i = 0; i < 100; i++)
    {
        int idx = 0;
        getline(cin, line);
        istringstream iss(line);

        while (iss >> num)
        {
            LADDER[i][idx++] = num;
        }
    }
}
int main()
{
    ios::sync_with_stdio(false);	// 입출력 속도 개선
    cin.tie(nullptr);

    for (int tc = 1; tc <= 10; tc++)
    {
        input();
        int x = 99;
        int goal, y, nx, ny;
        queue<pair<int, int> > q;

        for (int i = 0; i < 100; i++)
        {
            if (LADDER[99][i] == 2)
            {
                goal = i;
                y = i;
                break;
            }
        }

        visited[x][y] = true;
        q.push({ x, y });
        pair<int, int> cur = q.front();
        while (!q.empty())
        {
            cur = q.front();
            q.pop();
            if (cur.first == 0) break;

            for (int i = 0; i < 3; i++)
            {
                nx = cur.first + dx[i];
                ny = cur.second + dy[i];

                if (0 <= ny && ny < 100)
                {
                    if (!visited[nx][ny] && LADDER[nx][ny] == 1)
                    {
                        visited[nx][ny] = true;
                        q.push({ nx, ny });
                        break;
                    }
                }
            }
        }

        cout << "#" << tc << " " << ny << '\n';
    }
    return 0;
}