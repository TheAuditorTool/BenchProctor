// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("template-service")
export class PruneSubscription {
  @Post("pruneSubscription")
  async pruneSubscription(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.host as string) || "";
    const bulletin = `${heading}`;
    http.get(bulletin);
    return { created: true };
  }
}
