import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { schedulePayout } from "./payout_schedule";
import { collectReport } from "./collect_report";
import { compactIndex } from "./compact_index";
import { enrichDigest } from "./enrich_digest";
import { renderBatch } from "./render_batch";
import { normalizeSnapshot } from "./normalize_snapshot";
import { formatManifest } from "./format_manifest";
import { buildIndex } from "./build_index";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/schedulePayout", route(schedulePayout));
app.post("/collectReport", route(collectReport));
app.post("/compactIndex", route(compactIndex));
app.post("/enrichDigest", route(enrichDigest));
app.post("/renderBatch", route(renderBatch));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/formatManifest", route(formatManifest));
app.post("/buildIndex", route(buildIndex));

app.listen(3000, "0.0.0.0");
