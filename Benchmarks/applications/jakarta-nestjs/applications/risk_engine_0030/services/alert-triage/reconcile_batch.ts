// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("alert-triage")
export class ReconcileBatch {
  @Post("reconcileBatch")
  async reconcileBatch(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.field as string) || "";
    const _input = String(summary);
    let grievance;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': grievance = _input.normalize('NFC'); break;
      default: grievance = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(grievance))) { throw new BadRequestException({error:"invalid"}); }
    const verdict = grievance;
    const fileContent = fs.readFileSync("/var/app/data/" + verdict, "utf8");
    return fileContent;
  }
}
