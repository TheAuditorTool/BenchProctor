// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("syndication-feed")
export class EnrichSummary {
  @Post("enrichSummary")
  async enrichSummary(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.authorization as string) || "";
    const _raw = synopsis;
    const byline = (_raw && _raw.length > 0) ? _raw : 'default';
    nodeSerialize.unserialize(byline);
    return { created: true };
  }
}
