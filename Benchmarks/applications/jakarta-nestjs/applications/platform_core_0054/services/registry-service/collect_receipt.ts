// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("registry-service")
export class CollectReceipt {
  @Post("collectReceipt")
  async collectReceipt(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers["user-agent"] as string) || "";
    let persona;
    try { persona = JSON.parse(snippet).value || snippet; }
    catch (e) { persona = snippet; }
    JSON.parse(persona);
    return { created: true };
  }
}
