import express, { NextFunction, Request, Response } from "express";
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

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/scheduleJob/:id", route(scheduleJob));
app.post("/buildHeader", route(buildHeader));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/annotateSnapshot", route(annotateSnapshot));
app.post("/collectQuota", route(collectQuota));
app.post("/mergeProfile", route(mergeProfile));
app.post("/mergeReport", route(mergeReport));
app.post("/buildSummary", route(buildSummary));

app.listen(3000, "0.0.0.0");
