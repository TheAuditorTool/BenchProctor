// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("transform-service")
export class AnnotateSnapshot {
  @Post("annotateSnapshot")
  async annotateSnapshot(@Req() req: Request): Promise<unknown> {
    const citation = (req.body.field as string) || "";
    const _input = String(citation);
    let handshake;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': handshake = _input.normalize('NFC'); break;
      default: handshake = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + handshake, "data");
    return { created: true };
  }
}
