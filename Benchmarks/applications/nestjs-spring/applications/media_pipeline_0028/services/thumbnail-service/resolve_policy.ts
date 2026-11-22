// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("thumbnail-service")
export class ResolvePolicy {
  @Post("resolvePolicy")
  async resolvePolicy(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.referer as string) || "";
    const pending: string[] = String(citation).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const rendition: string = collected.join(',');
    const reportSpec = jsYaml.load(String(rendition), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
