#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
#define INF 1000000004
#define clarr(a) memset(a,0,sizeof(a))
#define fs first
#define sc second
#define mp make_pair
#define pb push_back

int sum_load(int *load, int n){
	int acc = 0;
	for (int i=0; i<n; ++i){
		acc += load[i];
	}
	return acc;
}

int main(int argc, char const *argv[]){
	ios_base::sync_with_stdio(false);

	int r,c,D,T,max_W, W, P, C;
	cin >> r >> c >> D >> T >> max_W;
	cin >> P;
	int product_weights[P];
	for (int i=0; i<P; ++i) cin >> product_weights[i];

	cin >> W;
	ii warehouses_pos[W];
	int stock[W][P];
	for (int i=0; i<W; ++i){
		cin >> warehouses_pos[i].fs >> warehouses_pos[i].sc;
		for (int j=0; j<P; ++j){
			cin >> stock[i][j];
		}
	}

	cin >> C;
	ii order_pos[C];
	int order_products[C][P];
	clarr(order_products);
	int kk,kkk;
	for (int i=0; i<C; ++i){
		cin >> order_pos[i].fs >> order_pos[i].sc;
		cin >> kkk;
		for (int k=0; k<kkk; ++k){
			cin >> kk;
			order_products[i][kk]++;
		}
	}

	for (int i=0; i<C; ++i){
		for (int j=0; j<P; ++j){
			cout << order_products[i][j] << " ";
		}
		cout << "\n";
	}

	int drone_pos = 0;
	int drone_load[P];
	clarr(drone_load);

	stringstream res;
	int commands = 0;

	// order i product j drone k
	for (int i=0; i<C; ++i){
		cout << "i=" << i << endl;
		for (int j=0; j<P; ++j){
			while (stock[drone_pos][j] > 0 && sum_load(drone_load, P) + product_weights[j] < max_W){
				stock[drone_pos][j]--;
				drone_load[j]++;
				if (drone_load[j] >= order_products[i][j]){
					cout << "pass\n";
					j++;
					while (order_products[i][j] == 0)j++;
				}
				if (j>=P) break;
			}
			// Load items
			for (int item=0; item<P; ++item){
				if (drone_load[item] > 0){
					res << "0 L " << drone_pos << " " << item << " " << drone_load[item] << endl;
					commands++;
				}
			}
			// Deliver
			for (int item=0; item<P; ++item){
				if (drone_load[item] > 0){
					res << "0 D " << i << " " << item << " " << drone_load[item] << endl;
					commands++;
				}
			}
			if (j>=P) break;

		}
	}

/*		for (int j=0; j<P; ++j){
			cout << "j=" << j << endl;
			if (order_products[i][j] > 0){
				cout << "order_products" << i << "," << j << ": " << order_products[i][j] << endl;
				for (int k=0; k<D; ++k){
					while (stock[drone_pos[k]][j] > 0 && (sum_load(drone_load[k], P) + product_weights[j]) < max_W){
						stock[drone_pos[k]][j]--;
						drone_load[k][j]++;
						if (drone_load[k][j] >= order_products[i][j]){
							cout << "pass\n";
							j++;
							while (order_products[i][j] == 0)j++;
						}
						cout << "while" << k << " " << drone_load[k][j] << endl;
						if (j>=P) break;
					}
					// Load items
					for (int item=0; item<P; ++item){
						if (drone_load[k][item] > 0){
							res << k << " L " << drone_pos[k] << " " << item << " " << drone_load[k][item] << endl;
							commands++;
						}
					}
					// Deliver
					for (int item=0; item<P; ++item){
						if (drone_load[k][item] > 0){
							res << k << " D " << drone_pos[k] << " " << i << " " << drone_load[k][item] << endl;
							commands++;
						}
					}
					if (j>=P) break;
				}
			}
		}
*/

	cout << commands << endl;
	cout << res.str();


	return 0;
}
