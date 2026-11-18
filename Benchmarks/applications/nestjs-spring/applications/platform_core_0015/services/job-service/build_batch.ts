// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("job-service")
export class BuildBatch {
  @Post("buildBatch")
  async buildBatch(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.origin as string) || "";
    const _input = String(note);
    let handshake;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': handshake = _input.normalize('NFC'); break;
      default: handshake = _input; break;
    }
    http.get(handshake);
    return { created: true };
  }
}
