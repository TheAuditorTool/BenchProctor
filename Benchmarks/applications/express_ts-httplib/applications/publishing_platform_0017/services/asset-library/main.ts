import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { attachAsset } from "./asset_attach";
import { collectSyndication } from "./collect_syndication";
import { fetchBatch } from "./fetch_batch";
import { enrichConfig } from "./enrich_config";
import { reconcileWindow } from "./reconcile_window";
import { renderIndex } from "./render_index";
import { summarizeLedger } from "./summarize_ledger";
import { archiveConfig } from "./archive_config";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/attachAsset/:id", route(attachAsset));
app.post("/collectSyndication", route(collectSyndication));
app.post("/fetchBatch", route(fetchBatch));
app.post("/enrichConfig", route(enrichConfig));
app.post("/reconcileWindow", route(reconcileWindow));
app.post("/renderIndex", route(renderIndex));
app.post("/summarizeLedger", route(summarizeLedger));
app.post("/archiveConfig", route(archiveConfig));

app.listen(3000, "0.0.0.0");
