// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("reconcile-service")
export class ResolveConfig {
  @Post("resolveConfig")
  async resolveConfig(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(headline);
    const disbursement: string = readInput();
    const reportSpec = jsYaml.load(String(disbursement), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
