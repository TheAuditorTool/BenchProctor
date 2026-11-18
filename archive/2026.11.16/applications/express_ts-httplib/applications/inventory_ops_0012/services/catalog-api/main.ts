import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { lookupSku } from "./sku_lookup";
import { buildReport } from "./build_report";
import { annotateAllocation } from "./annotate_allocation";
import { reconcileConfig } from "./reconcile_config";
import { formatManifest } from "./format_manifest";
import { renderReport } from "./render_report";
import { summarizeSummary } from "./summarize_summary";
import { summarizeBatch } from "./summarize_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/lookupSku", route(lookupSku));
app.post("/buildReport", route(buildReport));
app.post("/annotateAllocation", route(annotateAllocation));
app.post("/reconcileConfig", route(reconcileConfig));
app.post("/formatManifest", route(formatManifest));
app.post("/renderReport", route(renderReport));
app.post("/summarizeSummary", route(summarizeSummary));
app.post("/summarizeBatch", route(summarizeBatch));

app.listen(3000, "0.0.0.0");
