// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Query } from "@nestjs/common";
import { Response } from "express";
import * as nodeSerialize from "node-serialize";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

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
  @Post("BenchmarkTest00060")
  async BenchmarkTest00060(@Query("id") id: string): Promise<unknown> {
    const userInput = id || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    nodeSerialize.unserialize(data);
    return { created: true };
  }
}
