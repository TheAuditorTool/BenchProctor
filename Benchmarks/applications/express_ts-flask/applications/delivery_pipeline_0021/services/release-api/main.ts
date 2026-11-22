import express, { Request, Response } from "express";
import session from "express-session";

import { cutRelease } from "./release_cut";
import { publishSnapshot } from "./publish_snapshot";
import { mergeWindow } from "./merge_window";
import { enrichPolicy } from "./enrich_policy";
import { mergeHeader } from "./merge_header";
import { publishWindow } from "./publish_window";
import { buildIndex } from "./build_index";
import { loadPolicy } from "./load_policy";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/cutRelease", cutRelease);
app.post("/publishSnapshot", publishSnapshot);
app.post("/mergeWindow", mergeWindow);
app.post("/enrichPolicy/:id", enrichPolicy);
app.post("/mergeHeader", mergeHeader);
app.post("/publishWindow", publishWindow);
app.post("/buildIndex/:id", buildIndex);
app.post("/loadPolicy", loadPolicy);

app.listen(3000, "0.0.0.0");
