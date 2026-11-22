// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("watchlist-sync")
export class ReconcileCheckpoint {
  @Post("reconcileCheckpoint")
  async reconcileCheckpoint(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(excerpt);
    let verdict;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': verdict = _input.normalize('NFC'); break;
      default: verdict = _input; break;
    }
    const resolved = path.resolve("/var/app/data", verdict);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const grievance = resolved;
    fs.unlinkSync(grievance);
    return { created: true };
  }
}
