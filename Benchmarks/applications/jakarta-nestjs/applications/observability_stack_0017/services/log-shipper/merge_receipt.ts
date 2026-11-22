// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("log-shipper")
export class MergeReceipt {
  @Post("mergeReceipt")
  async mergeReceipt(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["x-forwarded-for"] as string) || "";
    const _input = String(note);
    let cohort;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': cohort = _input.normalize('NFC'); break;
      default: cohort = _input; break;
    }
    const resolved = path.resolve("/var/app/data", cohort);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const gauge = resolved;
    fs.unlinkSync(gauge);
    return { created: true };
  }
}
