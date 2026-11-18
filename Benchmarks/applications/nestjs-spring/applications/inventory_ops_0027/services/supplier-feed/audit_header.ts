// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("supplier-feed")
export class AuditHeader {
  @Post("auditHeader")
  async auditHeader(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["x-custom-header"] as string) || "";
    const _input = String(summary);
    let restock;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': restock = _input.normalize('NFC'); break;
      default: restock = _input; break;
    }
    net.connect(80, new URL(String(restock)).hostname);
    return { created: true };
  }
}
