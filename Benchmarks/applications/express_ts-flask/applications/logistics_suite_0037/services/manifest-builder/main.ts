import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { buildManifest } from "./manifest_build";
import { rotateWindow } from "./rotate_window";
import { validateSummary } from "./validate_summary";
import { pruneLabel } from "./prune_label";
import { archiveSnapshot } from "./archive_snapshot";
import { annotateRoster } from "./annotate_roster";
import { pruneConfig } from "./prune_config";
import { compactWaybill } from "./compact_waybill";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/buildManifest", route(buildManifest));
app.post("/rotateWindow", route(rotateWindow));
app.post("/validateSummary", route(validateSummary));
app.post("/pruneLabel", route(pruneLabel));
app.post("/archiveSnapshot", route(archiveSnapshot));
app.post("/annotateRoster", route(annotateRoster));
app.post("/pruneConfig", route(pruneConfig));
app.post("/compactWaybill", route(compactWaybill));

app.listen(3000, "0.0.0.0");
