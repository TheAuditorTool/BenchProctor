import express, { Request, Response } from "express";
import session from "express-session";

import { configureSample } from "./sample_config";
import { fetchConfig } from "./fetch_config";
import { annotateReport } from "./annotate_report";
import { compactIndex } from "./compact_index";
import { reconcileThreshold } from "./reconcile_threshold";
import { enrichSchedule } from "./enrich_schedule";
import { renderBundle } from "./render_bundle";
import { collectSample } from "./collect_sample";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/configureSample", configureSample);
app.post("/fetchConfig", fetchConfig);
app.post("/annotateReport", annotateReport);
app.post("/compactIndex", compactIndex);
app.post("/reconcileThreshold", reconcileThreshold);
app.post("/enrichSchedule", enrichSchedule);
app.post("/renderBundle", renderBundle);
app.post("/collectSample", collectSample);

app.listen(3000, "0.0.0.0");
