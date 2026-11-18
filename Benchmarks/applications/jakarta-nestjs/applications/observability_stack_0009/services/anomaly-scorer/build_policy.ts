// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("anomaly-scorer")
export class BuildPolicy {
  @Post("buildPolicy")
  async buildPolicy(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.payload as string) || "";
    const _raw = summary;
    const gauge = (_raw && _raw.length > 0) ? _raw : 'default';
    return "<div>" + gauge + "</div>";
  }
}
