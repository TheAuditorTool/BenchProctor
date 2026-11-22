// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("returns-service")
export class CollectFulfillment {
  @Post("collectFulfillment")
  async collectFulfillment(@Req() req: Request): Promise<unknown> {
    const notice = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(notice).split(',')) { parts.push(token); }
    const backorder: string = parts.join(',');
    const reportSpec = jsYaml.load(String(backorder), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
