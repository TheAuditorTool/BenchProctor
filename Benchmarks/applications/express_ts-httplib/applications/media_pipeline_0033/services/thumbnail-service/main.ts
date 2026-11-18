import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { renderThumbnail } from "./thumbnail_render";
import { collectManifest } from "./collect_manifest";
import { collectConfig } from "./collect_config";
import { normalizeReport } from "./normalize_report";
import { enrichReport } from "./enrich_report";
import { renderSnapshot } from "./render_snapshot";
import { loadLedger } from "./load_ledger";
import { pruneSnapshot } from "./prune_snapshot";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/renderThumbnail", route(renderThumbnail));
app.post("/collectManifest", route(collectManifest));
app.post("/collectConfig", route(collectConfig));
app.post("/normalizeReport", route(normalizeReport));
app.post("/enrichReport", route(enrichReport));
app.post("/renderSnapshot", route(renderSnapshot));
app.post("/loadLedger", route(loadLedger));
app.post("/pruneSnapshot", route(pruneSnapshot));

app.listen(3000, "0.0.0.0");
