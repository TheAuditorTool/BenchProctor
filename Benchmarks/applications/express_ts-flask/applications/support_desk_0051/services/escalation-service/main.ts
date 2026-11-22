import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { raiseEscalation } from "./escalation_raise";
import { resolveConfig } from "./resolve_config";
import { pruneReport } from "./prune_report";
import { archiveSurvey } from "./archive_survey";
import { exportManifest } from "./export_manifest";
import { mergeWindow } from "./merge_window";
import { loadReceipt } from "./load_receipt";
import { resolveWindow } from "./resolve_window";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/raiseEscalation/:id", route(raiseEscalation));
app.post("/resolveConfig", route(resolveConfig));
app.post("/pruneReport", route(pruneReport));
app.post("/archiveSurvey", route(archiveSurvey));
app.post("/exportManifest", route(exportManifest));
app.post("/mergeWindow/:id", route(mergeWindow));
app.post("/loadReceipt", route(loadReceipt));
app.post("/resolveWindow", route(resolveWindow));

app.listen(3000, "0.0.0.0");
