// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("redaction-service")
export class PublishLedger {
  @Post("publishLedger")
  async publishLedger(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.host as string) || "";
    const dossier = `${excerpt}`;
    http.get(dossier);
    return { created: true };
  }
}
