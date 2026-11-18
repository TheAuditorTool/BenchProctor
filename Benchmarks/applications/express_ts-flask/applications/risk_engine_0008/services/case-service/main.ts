import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { openCase } from "./case_open";
import { fetchCase } from "./fetch_case";
import { buildSummary } from "./build_summary";
import { rotateScreening } from "./rotate_screening";
import { reconcileThreshold } from "./reconcile_threshold";
import { loadIndex } from "./load_index";
import { collectRecord } from "./collect_record";
import { validateDigest } from "./validate_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/openCase", route(openCase));
app.post("/fetchCase", route(fetchCase));
app.post("/buildSummary", route(buildSummary));
app.post("/rotateScreening/:id", route(rotateScreening));
app.post("/reconcileThreshold", route(reconcileThreshold));
app.post("/loadIndex", route(loadIndex));
app.post("/collectRecord", route(collectRecord));
app.post("/validateDigest", route(validateDigest));

app.listen(3000, "0.0.0.0");
