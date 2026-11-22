// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("member-directory")
export class AnnotateSummary {
  @Post("annotateSummary")
  async annotateSummary(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers.authorization as string) || "";
    const _input = String(paragraph);
    let wording;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': wording = _input.normalize('NFC'); break;
      default: wording = _input; break;
    }
    fs.unlinkSync("/var/app/data/" + wording);
    return { created: true };
  }
}
