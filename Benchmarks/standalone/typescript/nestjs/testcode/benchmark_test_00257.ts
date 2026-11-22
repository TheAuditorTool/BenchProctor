// SPDX-License-Identifier: Apache-2.0
import { Controller, Param, Post } from "@nestjs/common";
import { Response } from "express";
import * as jsYaml from "js-yaml";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00257/:id")
  async BenchmarkTest00257(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const pending: string[] = String(userInput).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const data: string = collected.join(',');
    const reportSpec = jsYaml.load(String(data), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
