// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00699")
  async BenchmarkTest00699(@Headers("x-forwarded-for") xff: string): Promise<unknown> {
    const userInput = xff || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
    eval(processed);
    return { created: true };
  }
}
