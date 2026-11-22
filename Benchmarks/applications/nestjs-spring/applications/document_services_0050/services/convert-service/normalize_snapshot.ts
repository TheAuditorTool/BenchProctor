// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("convert-service")
export class NormalizeSnapshot {
  @Post("normalizeSnapshot")
  async normalizeSnapshot(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const _input = String(citation);
    let dossier;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': dossier = _input.normalize('NFC'); break;
      default: dossier = _input; break;
    }
    fs.unlinkSync("/var/app/data/" + dossier);
    return { created: true };
  }
}
