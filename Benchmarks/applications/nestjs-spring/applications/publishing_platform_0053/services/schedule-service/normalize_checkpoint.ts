// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("schedule-service")
export class NormalizeCheckpoint {
  @Post("normalizeCheckpoint")
  async normalizeCheckpoint(@Req() req: Request): Promise<unknown> {
    const note = (req.body.field as string) || "";
    const _input = String(note);
    let byline;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': byline = _input.normalize('NFC'); break;
      default: byline = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + byline, "data");
    return { created: true };
  }
}
