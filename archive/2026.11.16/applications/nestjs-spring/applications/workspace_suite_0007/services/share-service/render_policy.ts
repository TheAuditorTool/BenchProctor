// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("share-service")
export class RenderPolicy {
  @Post("renderPolicy")
  async renderPolicy(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const subtitle: string = normalize(summary);
    return "<div>" + subtitle + "</div>";
  }
}
