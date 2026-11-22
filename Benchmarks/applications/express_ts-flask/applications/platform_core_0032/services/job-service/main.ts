import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { scheduleJob } from "./job_schedule";
import { buildHeader } from "./build_header";
import { publishCheckpoint } from "./publish_checkpoint";
import { annotateSnapshot } from "./annotate_snapshot";
import { collectQuota } from "./collect_quota";
import { mergeProfile } from "./merge_profile";
import { mergeReport } from "./merge_report";
import { buildSummary } from "./build_summary";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/scheduleJob", scheduleJob);
app.post("/buildHeader", buildHeader);
app.post("/publishCheckpoint", publishCheckpoint);
app.post("/annotateSnapshot", annotateSnapshot);
app.post("/collectQuota", collectQuota);
app.post("/mergeProfile/:id", mergeProfile);
app.post("/mergeReport", mergeReport);
app.post("/buildSummary/:id", buildSummary);

app.listen(3000, "0.0.0.0");
