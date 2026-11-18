import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { startRecovery } from "./recovery_start";
import { summarizeBundle } from "./summarize_bundle";
import { mergeThreshold } from "./merge_threshold";
import { resolveBatch } from "./resolve_batch";
import { reconcileConfig } from "./reconcile_config";
import { publishConfig } from "./publish_config";
import { renderReport } from "./render_report";
import { exportHeader } from "./export_header";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/startRecovery", route(startRecovery));
app.post("/summarizeBundle", route(summarizeBundle));
app.post("/mergeThreshold", route(mergeThreshold));
app.post("/resolveBatch", route(resolveBatch));
app.post("/reconcileConfig", route(reconcileConfig));
app.post("/publishConfig", route(publishConfig));
app.post("/renderReport", route(renderReport));
app.post("/exportHeader", route(exportHeader));

app.listen(3000, "0.0.0.0");
