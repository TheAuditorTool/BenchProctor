import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { scheduleJob } from "./job_schedule";
import { annotateQuota } from "./annotate_quota";
import { buildBatch } from "./build_batch";
import { compactBatch } from "./compact_batch";
import { summarizeProfile } from "./summarize_profile";
import { annotateSchedule } from "./annotate_schedule";
import { buildIndex } from "./build_index";
import { mergeSnapshot } from "./merge_snapshot";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/scheduleJob", route(scheduleJob));
app.post("/annotateQuota/:id", route(annotateQuota));
app.post("/buildBatch", route(buildBatch));
app.post("/compactBatch", route(compactBatch));
app.post("/summarizeProfile", route(summarizeProfile));
app.post("/annotateSchedule", route(annotateSchedule));
app.post("/buildIndex", route(buildIndex));
app.post("/mergeSnapshot", route(mergeSnapshot));

app.listen(3000, "0.0.0.0");
