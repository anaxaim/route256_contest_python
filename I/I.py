# include <algorithm>
# include <cmath>
# include <cstdlib>
# include <ctime>
# include <iostream>
# include <limits>
# include <map>
# include <numeric>
# include <queue>
# include <set>
# include <stack>
# include <string>
# include <unordered_map>
# include <unordered_set>
# include <vector>

using
namespace
std;

struct
Event
{
    int64_t
t;
int
l;
int64_t
d;
int
a;
};

bool
operator < (const Event & lhs, const Event & rhs)
{
return lhs.d < rhs.d;
}

bool
operator > (const Event & lhs, const Event & rhs)
{
return lhs.d > rhs.d;
}

int
main()
{
int
n, m;
cin >> n >> m;

priority_queue < int, vector < int >, greater < int >> pqa;
for (int i = 0; i < n; ++i)
    {
        int
    a;
    cin >> a;
    pqa.push(a);
    }

    priority_queue < Event, vector < Event >, greater < Event >> pqe;

    int64_t
    res = 0;

    for (int task = 0; task < m; ++task)
        {
            Event
        ev = {0, 0, 0, 0};
        cin >> ev.t >> ev.l;
        ev.d = ev.t + ev.l;

    while (!pqe.empty())
    {
        Event
    topEv = pqe.top();
    if (ev.t >= topEv.d)
    {
    res += (int64_t)topEv.l * topEv.a;
    pqe.pop();
    pqa.push(topEv.a);
    }
    else {
    break;
    }
    }

    if (pqa.empty())
    {
    continue;
    }
    else
    {
    int64_t
    topA = pqa.top();
    pqa.pop();
    ev.a = topA;
    pqe.push(ev);
    }
    }

    while (!pqe.empty())
    {
        Event
    topEv = pqe.top();
    pqe.pop();
    res += (int64_t)
    topEv.l * topEv.a;
    }

    cout << res;
    return 0;
    }

    # / *
    #
    # 3
    # 7
    # 1
    # 1
    # 1
    # 1
    # 3
    # 2
    # 5
    # 3
    # 7
    # 4
    # 1
    # 5
    # 5
    # 6
    # 1
    # 9
    # 2
    #
    # * /
    #
