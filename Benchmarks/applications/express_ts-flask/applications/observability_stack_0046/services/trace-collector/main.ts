import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { collectTrace } from "./trace_collect";
import { fetchReport } from "./fetch_report";
import { pruneDigest } from "./prune_digest";
import { compactSchedule } from "./compact_schedule";
import { formatProfile } from "./format_profile";
import { collectMetric } from "./collect_metric";
import { pruneProfile } from "./prune_profile";
import { summarizeRoster } from "./summarize_roster";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/collectTrace", collectTrace);
app.post("/fetchReport", fetchReport);
app.post("/pruneDigest", pruneDigest);
app.post("/compactSchedule", compactSchedule);
app.post("/formatProfile", formatProfile);
app.post("/collectMetric", collectMetric);
app.post("/pruneProfile", pruneProfile);
app.post("/summarizeRoster/:id", summarizeRoster);

app.listen(3000, "0.0.0.0");
