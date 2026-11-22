import express, { Request, Response } from "express";
import session from "express-session";

import { buildManifest } from "./stream_manifest";
import { enrichSchedule } from "./enrich_schedule";
import { loadCaption } from "./load_caption";
import { validateBundle } from "./validate_bundle";
import { prunePolicy } from "./prune_policy";
import { archiveRecord } from "./archive_record";
import { mergeReceipt } from "./merge_receipt";
import { fetchConfig } from "./fetch_config";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/buildManifest", buildManifest);
app.post("/enrichSchedule/:id", enrichSchedule);
app.post("/loadCaption", loadCaption);
app.post("/validateBundle", validateBundle);
app.post("/prunePolicy", prunePolicy);
app.post("/archiveRecord", archiveRecord);
app.post("/mergeReceipt", mergeReceipt);
app.post("/fetchConfig", fetchConfig);

app.listen(3000, "0.0.0.0");
