batch_result = df.nlargest(int(params["# rows"]), attributes["target"][0]) 

self.top = pd.concat([self.top, batch_result], axis=0).nlargest(int(params["# rows"]), attributes["target"][0]) if self.top is not None else batch_result
return self.top