import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { cutRelease } from "./release_cut";
import { publishSnapshot } from "./publish_snapshot";
import { mergeWindow } from "./merge_window";
import { buildSummary } from "./build_summary";
import { mergeCanary } from "./merge_canary";
import { normalizeConfig } from "./normalize_config";
import { formatSummary } from "./format_summary";
import { exportReport } from "./export_report";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/cutRelease", route(cutRelease));
app.post("/publishSnapshot", route(publishSnapshot));
app.post("/mergeWindow", route(mergeWindow));
app.post("/buildSummary", route(buildSummary));
app.post("/mergeCanary", route(mergeCanary));
app.post("/normalizeConfig", route(normalizeConfig));
app.post("/formatSummary", route(formatSummary));
app.post("/exportReport", route(exportReport));

app.listen(3000, "0.0.0.0");
