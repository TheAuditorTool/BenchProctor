// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("returns-service")
export class CompactWindow {
  @Post("compactWindow")
  async compactWindow(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const _raw = citation;
    const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
    nodeSerialize.unserialize(backorder);
    return { created: true };
  }
}
