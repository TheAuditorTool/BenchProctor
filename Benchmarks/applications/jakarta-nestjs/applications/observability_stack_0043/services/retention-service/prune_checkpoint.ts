// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("retention-service")
export class PruneCheckpoint {
  @Post("pruneCheckpoint")
  async pruneCheckpoint(@Req() req: Request): Promise<unknown> {
    const note = (req.body.field as string) || "";
    const _input = String(note);
    let gauge;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': gauge = _input.normalize('NFC'); break;
      default: gauge = _input; break;
    }
    if (!/^(asc|desc|name|created)$/.test(String(gauge))) { throw new BadRequestException({error:"invalid"}); }
    const cohort = gauge;
    const fileContent = fs.readFileSync("/var/app/data/" + cohort, "utf8");
    return fileContent;
  }
}
